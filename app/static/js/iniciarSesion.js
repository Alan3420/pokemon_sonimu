
function iniciarSesion() {
  // Abre una nueva ventana
  const nuevaVentana = window.open("", "loginWindow", "width=400,height=300");

  // Escribe el formulario dentro de la nueva ventana
  nuevaVentana.document.write(`
    <form method="POST" action="/pokedex">
    <label for="nombre">Usuarios</label><br> 
    <input type="text" name="nombre" id="nombre"> 
    <label for="password">Contraseña</label><br> 
    <input type="password" name="password" id="contraseña"><br> 
    <button type="submit">Iniciar Sesion</button> </form>
  `);
}