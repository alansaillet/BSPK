import * as THREE from 'three';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';// Define variables

// Define variables
let scene, camera, renderer, model;

// Initialize Three.js scene
function init() {
    // Create a scene
    scene = new THREE.Scene();

    // Create a camera
    camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    camera.position.z = 5;

    // Create a renderer
    renderer = new THREE.WebGLRenderer({ canvas: document.getElementById('myCanvas'), antialias: true });
    renderer.setClearColor("rgb(20,20,20)");
    renderer.setSize(window.innerWidth, window.innerHeight);

    //Filepath

    // Define the default static GLTF path
    let defaultGltfPath = '/static/out.gltf';

    // Try to get the dynamic GLTF URL from the HTML element
    const gltfUrlElement = document.getElementById('gltfUrl');
    let gltfPath = defaultGltfPath; // Use the default path initially

    // Check if the element exists and has a non-empty URL
    if (gltfUrlElement && gltfUrlElement.getAttribute('data-url')) {
        gltfPath = gltfUrlElement.getAttribute('data-url'); // Use the dynamic path if available
    }

    // Load GLTF model
    const loader = new GLTFLoader();
    console.log("test1")
    console.log(defaultGltfPath)
    console.log(gltfPath)
    loader.load(
        gltfPath,
        function(gltf) {
            model = gltf.scene;
            // Make the model grey
            const greyMaterial = new THREE.MeshBasicMaterial({ color: 0x888888 });
            model.traverse(child => {
                if (child.isMesh) {
                    child.material = greyMaterial;
                }
            });
            scene.add(model);
            zoomToFit(model);
        },
        undefined,
        function(error) {
            console.error(error);
        }
    );

    // Start animation loop
    animate();

}

// Animation loop
function animate() {
    requestAnimationFrame(animate);
    if (model) {
        model.rotation.x += 0.005;
        model.rotation.y += 0.01;
    }
    renderer.render(scene, camera);
}

function zoomToFit(object) {
    const box = new THREE.Box3().setFromObject(object);
    const size = box.getSize(new THREE.Vector3()).length();
    const center = box.getCenter(new THREE.Vector3());

    const direction = camera.position.clone().sub(center).normalize();
    camera.position.copy(direction.multiplyScalar(size * 1.2)).add(center);
    camera.lookAt(center.x, center.y, center.z);
}

// Call init() when the window is loaded
window.onload = init;
