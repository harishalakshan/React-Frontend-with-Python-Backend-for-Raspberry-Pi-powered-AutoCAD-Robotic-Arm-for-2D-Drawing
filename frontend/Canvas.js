
import React, { useRef, useState } from 'react';
import axios from 'axios';

function Canvas() {
  const canvasRef = useRef(null);
  const [drawing, setDrawing] = useState(false);
  const [coordinates, setCoordinates] = useState([]);

  const handleMouseDown = () => setDrawing(true);
  const handleMouseUp = () => setDrawing(false);

  const handleMouseMove = (e) => {
    if (!drawing) return;
    const canvas = canvasRef.current;
    const ctx = canvas.getContext('2d');
    const rect = canvas.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    ctx.lineTo(x, y);
    ctx.stroke();
    setCoordinates([...coordinates, { x: x / 5, y: y / 5 }]);
  };

  const sendDrawing = async () => {
    await axios.post('http://<raspberry-pi-ip>:5000/api/draw', { coordinates });
  };

  return (
    <div>
      <canvas
        ref={canvasRef}
        width={400}
        height={400}
        onMouseDown={handleMouseDown}
        onMouseUp={handleMouseUp}
        onMouseMove={handleMouseMove}
        style={{ border: '1px solid black' }}
      />
      <button onClick={sendDrawing}>Send Drawing</button>
    </div>
  );
}

export default Canvas;
