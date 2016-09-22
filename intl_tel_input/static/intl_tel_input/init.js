(function($) {
  var $el, options, $form, data, defaultCode,
      cssClass = '.intl-tel-input',
      forms = [],
      inputs = $(cssClass);

  inputs.each(function(i, el) {
    $el = $(el);
    data = $el.data();
    defaultCode = data.defaultCode !== undefined ? data.defaultCode : 'us';
    options = {
      initialCountry: "auto",
      geoIpLookup: function(callback) {
        $.get('//freegeoip.net/json/', function() {}, "jsonp").done(function(resp) {
          var countryCode = (resp && resp.country_code) ? resp.country_code : "";
          callback(countryCode);
        }).fail(function(jqXHR) {
          console.warn('GeoIP Error: ' + jqXHR.status);
          callback(defaultCode);
        });
      },
      allowDropdown: data.allowDropdown !== undefined ? true : false
    };

    options.utilsScript = 'https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/9.0.1/js/utils.js';

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
