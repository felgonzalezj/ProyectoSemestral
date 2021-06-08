
function confirmarDelete(id){
    Swal.fire({
        title: 'Esta seguro de eliminar?',
        text: "Usted no podra revertir esto!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si, Elimiar!'
      }).then((result) => {
        if (result.isConfirmed) {
          Swal.fire(
            'Eliminado!',
            'Su producto ha sido eliminado.',
            'success'
          ).then(function(){
              window.location.href = "/eliminar-producto/"+id+"/"
          })
        }
      })
}

function confirmarModificar(){
    Swal.fire({
        position: 'top-end',
        icon: 'success',
        title: 'Producto Modificado',
        showConfirmButton: false,
        timer: 1500
        
      })
}

function productoAgregado(){
  Swal.fire({
      position: 'top-end',
      icon: 'success',
      title: 'Producto Agregado',
      showConfirmButton: false,
      timer: 1500
    })
}