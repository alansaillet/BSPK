
class FieldTree {
    constructor(name) {
        this.name = name;
        this.subfields = [];
        this.parentConditionalValue = null; // Store parent choice's name
        this.element_id = "id_"+name
        this.isVisible = true
        this.parent = null;
    }

    addSubfield(parentConditionalValue, subfield) {
        subfield.parentConditionalValue = parentConditionalValue;
        subfield.parent = this
        this.subfields.push(subfield);
    }

    initialize() {
        // Find the DOM element corresponding to this field
        const element = document.getElementById(this.element_id);
        if (!element) return;

        element.addEventListener('change', () => {
                this.subfields.forEach(subfield => subfield.toggleVisibility(element.value));
            });
        // Initialize all subfields
        this.subfields.forEach(subfield => subfield.initialize());
        // Show or hide depending on initial value
        this.subfields.forEach(subfield => subfield.toggleVisibility(element.value));
    }

    toggleVisibility(parentSelectedValue) {
        const element = document.getElementById(this.element_id);
        if (!element) return;

        if (this.parentConditionalValue === parentSelectedValue && this.parent.isVisible == true) {
            this.isVisible = true
            element.disabled=false

            element.parentNode.style.display = ''; // Show
        } else {
            this.isVisible = false
            element.disabled=true

            element.parentNode.style.display = 'none'; // Hide
        }
        this.subfields.forEach(subfield => subfield.toggleVisibility(element.value));
    }
}

function createFieldTreesFromRules(rules) {
    let fields = {};

    // Helper function to get or create field
    function getField(name) {
        if (!fields[name]) {
            fields[name] = new FieldTree(name);
        }
        return fields[name];
    }

    rules.forEach(rule => {
        const [parentInfo, childInfos] = rule.split(">");
        const [parentName, parentValue] = parentInfo.split("=");
        const childNames = childInfos.split(",").map(name => name.trim());

        const parentField = getField(parentName);

        childNames.forEach(childName => {
            const childField = getField(childName);
            parentField.addSubfield(parentValue, childField);
        });
    });

    // Assuming the first rule's parent is the root
    const rootName = rules[0].split(">", 1)[0].split("=", 1)[0];
    return fields[rootName]; // Return the root field
}

// -------------------------------------------------------------
// ------- DEFINE VISIBILITY RULES HERE ------------------------
// -------------------------------------------------------------
const visibilityRules = [
    "furnituretype=table>width,length,height",
    "furnituretype=chair>chairbacktype",
    "chairbacktype=rods>nbrods",
    "chairbacktype=flat>thickness_backchair"
];
// -------------------------------------------------------------
// -------------------------------------------------------------
// -------------------------------------------------------------
document.addEventListener('DOMContentLoaded', () => {
    const rootFieldTree = createFieldTreesFromRules(visibilityRules);
    // Initialize and potentially other operations
    rootFieldTree.initialize();
});