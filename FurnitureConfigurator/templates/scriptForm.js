<script>
class FieldTree {
    constructor(name, field, element_id) {
        this.name = name;
        this.field = field;
        this.element_id = element_id; // Selector to find the corresponding DOM element
        this.subfields = [];
        this.parentChoice = null; // Store parent choice's name
    }

    addSubfield(parentChoice, subfield) {
        subfield.parentChoice = parentChoice;
        this.subfields.push(subfield);
    }

    initialize() {
        // Find the DOM element corresponding to this field
        const element = document.getElementById(this.element_id);
        if (!element) return;

        // If this is a choice field, add an event listener
        if (this.field.type === 'select') {
            element.addEventListener('change', () => {
                this.subfields.forEach(subfield => subfield.toggleVisibility(element.value));
            });
        }

        // Initialize all subfields
        this.subfields.forEach(subfield => subfield.initialize());
    }

    toggleVisibility(selectedValue) {
        const element = document.querySelector(this.element_id);
        if (!element) return;

        // Show or hide the element based on the parent choice
        if (this.parentChoice === selectedValue) {
            element.style.display = ''; // Show
        } else {
            element.style.display = 'none'; // Hide
        }

        // For select fields, reset value when hidden
        if (element.style.display === 'none' && this.field.type === 'select') {
            element.value = '';
            // Trigger change event to update dependent subfields
            element.dispatchEvent(new Event('change'));
        }
    }

    print() {
        console.log(this.parentChoice, this.name);
        this.subfields.forEach(subfield => subfield.print());
    }
}

</script>
