
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