function stripe_init() {
var stripe = Stripe('pk_test_HFRdaJ6niRE3L4WBTa5wzPt000oWDiJDop');
var elements = stripe.elements();

var style = {
    base: {
      color: "#32325d",
      lineHeight: '1.429'
    }
  };
  
  var card = elements.create("card", { style: style });
  card.mount("#card-element");

  card.addEventListener('change', ({error}) => {
    const displayError = document.getElementById('card-errors');
    if (error) {
      displayError.textContent = error.message;
    } else {
      displayError.textContent = '';
    }
  });

  var form = document.getElementById('payment_form');

  form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    console.log("PaymentForm Submitted")
    const clientSecret  = $('#id_cs').val()
    stripe.confirmCardPayment(clientSecret, {
      payment_method: {
        card: card,
        billing_details: {
          name: $('#id_full_name').val()
        }
      }
    }).then(function(result) {
      if (result.error) {
        Swal.fire({
          icon: 'error',
          title: 'Uh-Oh',
          html: '<p>'+ result.error.message + '</p>'
        })
      } else {
        // The payment has been processed!
        if (result.paymentIntent.status === 'succeeded') {
            console.info(result.paymentIntent);
            $.ajax({
                url: '/payment/orderconfirmed/',
                type: "POST",
                data: {
                    'full_name': $('#id_full_name').val(),
                    'street_address_1': $('#id_street_address1').val(),
                    'street_address_2': $('#id_street_address2').val(),
                    'town_or_city': $('#id_town_or_city').val(),
                    'county': $('#id_county').val(),
                    'country': $('#id_country').val(),
                    'confirmation_code': result.paymentIntent.id,
                    'amount': result.paymentIntent.amount,
                    'phone_number': $('#id_phone_number').val()
                },
                success: function(){
                    $('#payment-modal').modal('hide')
                    Swal.fire({
                        icon: 'success',
                        title: 'Payment completed',
                        html: '<h2>Thank you for purchasing</h2><hr/><p>You can use the link below to download the sofware</p><a class="btn btn-success" href="https://github.com/Lowe54/Support-Software-Inc/archive/master.zip">DOWNLOAD</a>',
                    })
                }
            })
        }
      };
  })
})
}
