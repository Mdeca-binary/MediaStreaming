const start_call = document.getElementById("startcall");

async function startCall(){
    const pc = new RTCPeerConnection();

    const dc = pc.createDataChannel("chat");
    dc.onopen = ()=> dc.send("Hello, world.");
    dc.onmessage = (e)=> console.log("Server says: ", e.data);

    const offer = await pc.createOffer();
    await pc.setLocalDescription(offer);

    const response = await fetch("http://127.0.0.1:8000/offer", {
        method: "POST", 
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({sdp: offer.sdp, type: offer.type})
    });
    const answer = await response.json();
    await pc.setRemoteDescription(new RTCSessionDescription(answer));
}