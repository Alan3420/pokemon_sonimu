
function iniciarSesion() {
  // Abre una nueva ventana
  const nuevaVentana = window.open("", "loginWindow", "width=400,height=300");

  // Escribe el formulario dentro de la nueva ventana
  nuevaVentana.document.write(`
    <form method="POST" action="/pokedex">
    <label for="nombre">Entrenador</label><br> 
    <input type="text" name="nombre" id="nombre"> 
    <button type="submit">Iniciar Sesion</button> </form>
  `);
}