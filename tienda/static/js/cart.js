var updateBtns = document.getElementsByClassName('update-cart')

for (var i = 0; i < updateBtns.length; i++ ){
    updateBtns[i].addEventListener('click', function() {
        var productoID = this.dataset.producto
        var action = this.dataset.action
        console.log('productoID:', productoID, 'action:', action )

        console.log('USER:', user)
        if(user=='AnonymousUser'){
            console.log('No esta logueado')
        }else{
            actualizarClienteCompra(productoID, action)
        }
    })

}
function actualizarClienteCompra(productoID, action) {
    console.log('Usuario logueado, enviando datos...')
    
    var url = '/Actualizar_Articulos/'
    
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-type': 'application/json',
            'X-CSRFToken': csrftoken,    
        },
        body: JSON.stringify({'productoID': productoID, 'action': action}),
    })    
    .then((response) => {
        return response.json();
    })
    .then((data) => {
        console.log('data:', data)
        console.log('productoID:', productoID);
        
        // Si la acción es 'remove', eliminar el producto del DOM
        if (action === 'remove') {
            var productoElemento = document.getElementById('producto-' + productoID);
            if (productoElemento) {
                productoElemento.remove();
            }
            return; // No hay más que hacer si se eliminó el producto
        }
        
        // Actualizar la cantidad del artículo en el carrito dinámicamente
        
        console.log('Buscando elemento con ID: cantidad-' + productoID);
        console.log('Elemento encontrado:', cantidadSpan);
        var cantidadSpan = document.getElementById('cantidad-' + productoID);
        
        if (cantidadSpan) {
            cantidadSpan.textContent = data.nueva_cantidad;
        }
        
        // Mostrar el mensaje al usuario si existe
        if (data.message) {
            alert(data.message);
        }
        
        // Actualizar la cantidad total de artículos en el carrito
        var totalArticulosSpan = document.getElementById('total-articulos');
        console.log('totalArticulosSpan:', totalArticulosSpan);
        if (totalArticulosSpan && data.total_articulos !== undefined) {
            totalArticulosSpan.textContent = data.total_articulos;
        } else {
            console.error('El elemento total-articulos no se encontró en el DOM o la clave total_articulos no está presente en la respuesta.');
        }
        
        console.log('Se actualizó la cantidad del artículo en el carrito dinámicamente');
    })
    .catch((error) => {
        console.error('Error during fetch:', error);
    });
}



