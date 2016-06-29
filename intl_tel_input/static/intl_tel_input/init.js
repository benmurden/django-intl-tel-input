(function($) {
  var $el, options, $form,
      cssClass = '.intl-tel-input',
      forms = [],
      inputs = $(cssClass);

  inputs.each(function(i, el) {
    $el = $(el);
    options = {
      initialCountry: "auto",
      geoIpLookup: function(callback) {
        $.get('http://ipinfo.io', function() {}, "jsonp").always(function(resp) {
          var countryCode = (resp && resp.country) ? resp.country : "";
          callback(countryCode);
        });
      }
    };

    if ($el.attr('data-utils-script')) {
      options['utilsScript'] = 'https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/9.0.1/js/utils.js';
    }

    $el.intlTelInput(options)
    .done(function() {
      $form = $el.closest('form');
      if (forms.indexOf($form) === -1) {
        $form.submit(function(e) {
          $form.find('input' + cssClass).val(function() {
            return $(this).intlTelInput("getNumber");
          });
        });

        forms.push($form);
      }
    });
  });
})(jQuery);
