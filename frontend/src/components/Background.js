import React, {useRef, useEffect} from "react";
import * as THREE from "three";
import {RectAreaLightHelper} from "three/examples/jsm/helpers/RectAreaLightHelper";
import {gsap, Power2, Power4} from "gsap";

const Background = () => {
    const canvasRef = useRef();

    useEffect(() => {
        const camera = new THREE.PerspectiveCamera(15, window.innerWidth / window.innerHeight, 1, 500);
        let INTERSECTED;
        const maxSize = 0.04; // Change this value to adjust the maximum size
        const canvasElem = canvasRef.current;

        const renderer = new THREE.WebGLRenderer({canvas: canvasElem});
        renderer.setPixelRatio(window.devicePixelRatio);

        renderer.setSize(window.innerWidth, window.innerHeight);
        renderer.shadowMap.enabled = false;
        renderer.shadowMap.type = THREE.PCFSoftShadowMap;
        renderer.shadowMap.needsUpdate = true;

        window.addEventListener('resize', onWindowResize, false);

        function onWindowResize() {
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
        }


        const scene = new THREE.Scene();
        const cameraRange = 3;

        const setcolor = 0x000000;

        scene.background = new THREE.Color(setcolor)
        scene.fog = new THREE.Fog(setcolor, 2.5, 3.5);

        //-------------------------------------------------------------- SCENE

        const sceneGroup = new THREE.Object3D();
        const particularGroup = new THREE.Object3D();
        const modularGroup = new THREE.Object3D();

        function generateParticle(num, amp = 2) {
            const gmaterial = new THREE.MeshPhysicalMaterial({color: 0xFFFFFF, side: THREE.DoubleSide});

            const gparticular = new THREE.CircleGeometry(0.2, 5);

            for (let i = 1; i < num; i++) {
                const pscale = 0.001 + Math.abs(mathRandom(0.03));
                const particular = new THREE.Mesh(gparticular, gmaterial);
                particular.position.set(mathRandom(amp), mathRandom(amp), mathRandom(amp));
                particular.rotation.set(mathRandom(), mathRandom(), mathRandom());
                particular.scale.set(pscale, pscale, pscale);
                particular.speedValue = mathRandom(1);

                particularGroup.add(particular);
            }
        }

        generateParticle(0, 2);

        sceneGroup.add(particularGroup);
        scene.add(modularGroup);
        scene.add(sceneGroup);

        function mathRandom(num = 1) {
            var setNumber = -Math.random() * num + Math.random() * num;
            return setNumber;
        }

        //-------------------------------------------------------------- LINES

        function randomTimeout(min, max) {
            return Math.random() * (max - min) + min;
        }

        const linesBetweenIcosahedrons = [];

        function getSurfacePoint(icosahedron1, icosahedron2, scale) {
            const direction = new THREE.Vector3().subVectors(icosahedron2.position, icosahedron1.position);
            const length = direction.length();
            direction.normalize();
            const distance = scale * 0.5 * Math.sin(Math.PI / 3); // Icosahedron edge length
            return direction.multiplyScalar(length - distance).add(icosahedron1.position);
        }

        function addLinesBetweenIcosahedrons() {
            const icosahedrons = modularGroup.children;
            const lineMaterial = new THREE.LineBasicMaterial({
                color: 0x588784,
            });
            const lineGeometry = new THREE.BufferGeometry();

            const randomIndex1 = Math.floor(Math.random() * icosahedrons.length);
            const randomIndex2 = Math.floor(Math.random() * icosahedrons.length);

            if (randomIndex1 === randomIndex2) {
                return;
            }

            const icosahedron1 = icosahedrons[randomIndex1];
            const icosahedron2 = icosahedrons[randomIndex2];

            const positions = new Float32Array(6); // Initialize with size 6

            lineGeometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
            const line = new THREE.Line(lineGeometry, lineMaterial);
            scene.add(line);

            // Store the line and connected Icosahedrons
            const lineObject = {line, icosahedron1, icosahedron2};
            linesBetweenIcosahedrons.push(lineObject);

            // Remove the line after a random duration
            setTimeout(() => {
                scene.remove(line);
                const index = linesBetweenIcosahedrons.indexOf(lineObject);
                if (index > -1) {
                    linesBetweenIcosahedrons.splice(index, 1);
                }
            }, randomTimeout(5000, 10000)); // Change these values to control the duration range
        }

        function updateLinePositionsHelper(line, icosahedron1, icosahedron2) {
            const scale1 = icosahedron1.scale.x;
            const scale2 = icosahedron2.scale.x;

            const startPoint = getSurfacePoint(icosahedron1, icosahedron2, scale1);
            const endPoint = getSurfacePoint(icosahedron2, icosahedron1, scale2);

            const positions = line.geometry.attributes.position.array;
            positions[0] = startPoint.x;
            positions[1] = startPoint.y;
            positions[2] = startPoint.z;
            positions[3] = endPoint.x;
            positions[4] = endPoint.y;
            positions[5] = endPoint.z;
            line.geometry.attributes.position.needsUpdate = true;
            line.material.opacity = 0.5;

            // Check for intersections
            const raycaster = new THREE.Raycaster();
            raycaster.set(icosahedron1.position, icosahedron2.position.clone().sub(icosahedron1.position).normalize());
            const intersects = raycaster.intersectObjects(modularGroup.children);
            const isIntersecting = intersects.some(intersect => intersect.object !== icosahedron1 && intersect.object !== icosahedron2);

            if (isIntersecting) {
                // If intersecting, set opacity to 0
                line.material.opacity = 0;
            } else {
                // If not intersecting, set opacity back to 1
                line.material.opacity = 1;
            }
        }

        function updateLinePositions() {
            linesBetweenIcosahedrons.forEach(lineObject => {
                const {line, icosahedron1, icosahedron2} = lineObject;
                updateLinePositionsHelper(line, icosahedron1, icosahedron2);
            });
        }


        //------------------------------------------------------------- INIT
        function init() {
            for (let i = 0; i < 35; i++) {
                const geometry = new THREE.IcosahedronGeometry(1);
                const material = new THREE.MeshStandardMaterial({
                    flatShading: false,
                    color: 0xFFFFFF,
                    transparent: true,
                    opacity: 0.3,
                    wireframe: true
                });
                let icosahedron;
                icosahedron = new THREE.Mesh(geometry, material);

                // Add Sphere
                const subGeometry = new THREE.IcosahedronGeometry(0.45, );
                const sphereMaterial = new THREE.MeshPhongMaterial({color: 0x239e96});
                const sphere = new THREE.Mesh(subGeometry, sphereMaterial);
                icosahedron.add(sphere);

                icosahedron.speedRotation = Math.random() * 0.1;
                icosahedron.positionX = mathRandom();
                icosahedron.positionY = mathRandom();
                icosahedron.positionZ = mathRandom();
                icosahedron.castShadow = true;
                icosahedron.receiveShadow = true;

                const newScaleValue = Math.max(mathRandom(maxSize), 0.03);

                icosahedron.scale.set(newScaleValue, newScaleValue, newScaleValue);
                //---
                icosahedron.rotation.x = mathRandom(180 * Math.PI / 180);
                icosahedron.rotation.y = mathRandom(180 * Math.PI / 180);
                icosahedron.rotation.z = mathRandom(180 * Math.PI / 180);
                //
                icosahedron.position.set(icosahedron.positionX, icosahedron.positionY, icosahedron.positionZ);
                modularGroup.add(icosahedron);

                function scheduleAddLine() {
                    setTimeout(() => {
                        addLinesBetweenIcosahedrons();
                        scheduleAddLine();
                    }, randomTimeout(3000, 5000)); // Change these values to control the duration range
                }
                const addLine = mathRandom();
                if (addLine > 0.4) {
                    scheduleAddLine();
                }
            }
        }

        //------------------------------------------------------------- CAMERA
        camera.position.set(0, 0, cameraRange);
        let cameraValue = false;

        function cameraSet() {
            if (!cameraValue) {
                gsap.to(camera.position, 1, {z: cameraRange, ease: Power4.easeInOut});
                cameraValue = true;
            } else {
                gsap.to(camera.position, 1, {z: cameraRange, x: 0, y: 0, ease: Power4.easeInOut});
                INTERSECTED = null;
                cameraValue = false;
            }
        }

        function onKeyPress(event) {
            if (event.code === "Space") {
                cameraSet();
            }
        }

        window.addEventListener('keydown', onKeyPress, false);

        //------------------------------------------------------------- LINES

        //------------------------------------------------------------- SCENE
        const ambientLight = new THREE.AmbientLight(0xFFFFFF, 0.1);
        scene.add(ambientLight);

        var light = new THREE.SpotLight(0xFFFFFF, 3);
        light.position.set(5, 5, 2);
        light.castShadow = true;
        light.shadow.mapSize.width = 10000;
        light.shadow.mapSize.height = light.shadow.mapSize.width;
        light.penumbra = 0.5;

        const lightBack = new THREE.PointLight(0xa8275b, 10);
        lightBack.position.set(0, -3, -1);

        scene.add(sceneGroup);
        scene.add(light);
        scene.add(lightBack);

        const rectSize = 2;
        const intensity = 100;
        const rectLight = new THREE.RectAreaLight(0xFFFFFF, intensity, rectSize, rectSize);
        rectLight.position.set(0, 0, 1);
        rectLight.lookAt(0, 0, 0);

        let rectLightHelper;
        rectLightHelper = new RectAreaLightHelper(rectLight);
        scene.add(rectLightHelper);

        //------------------------------------------------------------- RAYCASTER
        const raycaster = new THREE.Raycaster();
        let mouse = new THREE.Vector2();
        let intersected;


        //------------------------------------------------------------- RENDER
        const uSpeed = 0.1;

        function animate() {
            let i;
            let l;
            const time = performance.now() * 0.0003;
            requestAnimationFrame(animate);
            //---
            for (; i < l; i++) {
                const newObject = particularGroup.children[i];
                newObject.rotation.x += newObject.speedValue / 10;
                newObject.rotation.y += newObject.speedValue / 10;
                newObject.rotation.z += newObject.speedValue / 10;
                //---
                //newObject.position.y = Math.sin(time) * 3;
            }


            i = 0;
            l = modularGroup.children.length;
            for (; i < l; i++) {
                const newCubes = modularGroup.children[i];
                newCubes.rotation.x += 0.008;
                newCubes.rotation.y += 0.005;
                newCubes.rotation.z += 0.003;
                //---
                newCubes.position.x = Math.sin(time * newCubes.positionZ) * newCubes.positionY;
                newCubes.position.y = Math.cos(time * newCubes.positionX) * newCubes.positionZ;
                newCubes.position.z = Math.sin(time * newCubes.positionY) * newCubes.positionX;
            }
            //---
            particularGroup.rotation.y += 0.005;
            //---
            modularGroup.rotation.y -= ((mouse.x * 4) + modularGroup.rotation.y) * uSpeed;
            modularGroup.rotation.x -= ((-mouse.y * 4) + modularGroup.rotation.x) * uSpeed;
            updateLinePositions();

            camera.lookAt(scene.position);
            renderer.render(scene, camera);
        }

        animate();
        init();
    }, []);

    return <canvas ref={canvasRef} style={{position: "fixed", zIndex: -1}}/>;
};

export default Background;