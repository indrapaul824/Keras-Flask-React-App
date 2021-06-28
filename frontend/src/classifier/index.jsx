import React, { useEffect, useRef, useState } from "react";


const Classifier = () => {
    const canvasRef = useRef();
    const imageRef = useRef();
    const videoRef = useRef();

    const [result, setResult] = useState("");

    useEffect(() => {
        // TODO: Fetch camera feed here.
    }, []);

    useEffect(() => {
        // TODO: Send images to API here
    }, []);

    return (
        <>
            <h1>Image Classifier</h1>
            <div></div>
        </>
    )
};


export default Classifier;