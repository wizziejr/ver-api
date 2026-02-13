
function createCert(event) {
    alert(7777);

    event.preventDefault();
    const cert_id = document.getElementById("cert_id").value;
    const name = document.getElementById("name").value;
    const qualification = document.getElementById("qualification").value;
    const response = fetch("/cert/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            cert_id,
            name,
            qualification,
        }),
    });
    const data = response.json();
    console.log(data);
}