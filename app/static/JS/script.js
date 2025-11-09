// Espera a que todo el HTML esté cargado
document.addEventListener('DOMContentLoaded', () => {

    // --- 1. Referencias a Elementos (usando tus nuevos IDs) ---
    const donateForm = document.getElementById('donate-form');
    const recipientWallet = document.querySelector('.donate-wallet').innerText;
    const senderWalletInput = document.getElementById('payerWallet');
    const payButton = document.getElementById('payBtn');
    const amountButtons = document.querySelectorAll('.amount-chips button[data-amount]');
    const otherAmountInput = document.getElementById('amountInput');
    const statusDiv = document.getElementById('donate-status');

    let selectedAmount = 0;
    const assetCode = 'USD'; // Cambia esto si tu wallet de prueba usa MXN
    const assetScale = 2;      // 2 decimales (centavos)

    // --- 2. Lógica de Selección de Monto ---

    // Maneja clic en botones de monto fijo
    amountButtons.forEach(button => {
        button.addEventListener('click', () => {
            // Obtiene el monto del atributo 'data-amount'
            selectedAmount = parseInt(button.dataset.amount, 10);
            otherAmountInput.value = ''; // Limpia el input "Otro"
            
            // Lógica visual para resaltar el botón seleccionado
            amountButtons.forEach(btn => btn.classList.remove('active')); // 'active' es una clase común de Bootstrap
            button.classList.add('active');
        });
    });

    // Maneja escritura en el input "Otro"
    otherAmountInput.addEventListener('input', () => {
        selectedAmount = 0; // Deselecciona botones fijos
        amountButtons.forEach(btn => btn.classList.remove('active'));
    });

    // --- 3. Lógica del Botón de Pago ---
    // Usamos el evento 'submit' del formulario
    donateForm.addEventListener('submit', async (event) => {
        // ¡Evita que el formulario se envíe de la forma tradicional!
        event.preventDefault(); 

        // Mostrar estado de carga
        payButton.disabled = true;
        statusDiv.innerText = 'Procesando pago, por favor espera...';
        statusDiv.hidden = false;

        // Determina el monto final
        const customAmount = parseFloat(otherAmountInput.value);
        const amountToPay = customAmount > 0 ? customAmount : selectedAmount;
        const senderWallet = senderWalletInput.value;

        // Validaciones
        if (amountToPay <= 0) {
            alert('Por favor, selecciona o ingresa un monto.');
            statusDiv.hidden = true;
            payButton.disabled = false;
            return;
        }
        if (!senderWallet || !senderWallet.startsWith('http')) {
            alert('Por favor, ingresa una URL de wallet válida para el patrocinador.');
            statusDiv.hidden = true;
            payButton.disabled = false;
            return;
        }

        // ¡Inicia el pago!
        await handlePayment(senderWallet, recipientWallet, amountToPay);
        
        // La página será redirigida; si falla, volvemos a habilitar el botón
        payButton.disabled = false;
        statusDiv.hidden = true;
    });

    // --- 4. Función de Pago (El núcleo de Open Payments) ---
    async function handlePayment(senderWalletUrl, recipientWalletUrl, amount) {
        
        // La librería se carga en el objeto 'window.InterledgerPay' desde el CDN
        const { createClient } = window.InterledgerPay;

        try {
            // 1. Crear el cliente con el wallet del *pagador*
            const client = await createClient({
                paymentPointerUrl: senderWalletUrl 
            });

            // 2. Crear una "quote" (cotización)
            const quote = await client.payment.quote({
                paymentPointerUrl: recipientWalletUrl, // El wallet que recibe
                amount: {
                    // Convertir a la unidad mínima (ej: $200 -> 20000 centavos)
                    value: (amount * Math.pow(10, assetScale)).toString(), 
                    assetCode: assetCode,
                    assetScale: assetScale
                }
            });

            // 3. Iniciar el pago (Esto REDIRIGIRÁ al usuario a su wallet)
            console.log('Redirigiendo al wallet del patrocinador para aprobación...');
            await client.payment.pay({
                quote: quote,
                // A dónde debe regresar el usuario después de aprobar/cancelar
                redirectUrl: window.location.href 
            });

        } catch (error) {
            console.error('Error en el pago con Open Payments:', error);
            statusDiv.innerText = `Error: ${error.message}`;
            statusDiv.hidden = false;
            payButton.disabled = false; // Vuelve a habilitar el botón si hay error
        }
    }

    // --- 5. Lógica para los otros botones ---
    document.getElementById('qrBtn').addEventListener('click', () => {
        alert(`Implementación pendiente: Generar QR para ${recipientWallet}`);
        // Aquí podrías usar una librería para generar un QR con la URL del 'recipientWallet'
    });

    document.getElementById('linkBtn').addEventListener('click', () => {
        navigator.clipboard.writeText(window.location.href);
        alert('Enlace de donación copiado al portapapeles');
    });
});