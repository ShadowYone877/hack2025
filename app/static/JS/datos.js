// $(document).ready() asegura que este código solo se ejecute
// cuando toda la página HTML se haya cargado.
$(document).ready(function() {
    
    // 1. Selecciona el 'row' donde irán las escuelas
    const $escuelasRow = $('#escuelas-row');

    // 2. Muestra un mensaje de carga mientras se hace la petición
    $escuelasRow.html('<p class="text-center">Cargando escuelas...</p>');

    // 3. Llama a tu API de Flask
    // $.getJSON es un atajo de jQuery para una petición GET que espera JSON
    $.getJSON('/getEscuela', function(escuelas) {
        
        // 4. Si la petición tiene éxito, limpia el mensaje de "cargando"
        $escuelasRow.empty();

        // 5. Recorre la lista de escuelas que vino en el JSON
        $.each(escuelas, function(index, escuela) {
            
            // 6. Crea el HTML para la tarjeta (thumbnail)
            // Se usan ` (backticks) para crear una plantilla de texto
            const tarjetaHtml = `
                <div class="col-md-4">
                    <div class="thumbnail">
                        <img src="${escuela.image}" alt="${escuela.name}">
                        <div class="caption">
                            <h3>${escuela.name}</h3>
                            <p>${escuela.description}</p>
                            <p><a href="#" class="btn btn-primary" role="button">Más información</a></p>
                        </div>
                    </div>
                </div>
            `;
            
            // 7. Añade la nueva tarjeta al 'row'
            $escuelasRow.append(tarjetaHtml);
        });

    }).fail(function() {
        // 8. Si la petición falla (ej. error 500 en Flask), muestra un error
        $escuelasRow.html('<p class="text-danger text-center">No se pudieron cargar las escuelas.</p>');
    });

});