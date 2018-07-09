(function($) {
  var options, data, defaultCode,
      cssClass = '.intl-tel-input',
      forms = [],
      inputs = $(cssClass);

  inputs.each(function(i, el) {
    var $el, $realInput, $form;

    $el = $(el);
    $realInput = $el.prev();
    data = $el.data();
    defaultCode = data.defaultCode !== undefined ? data.defaultCode : 'us';
    options = {
      initialCountry: data.autoGeoIp!== undefined ? 'auto' : data.defaultCode,
      geoIpLookup: function(callback) {
        if (data.autoGeoIp!== undefined) {
          $.get('//freegeoip.net/json/', function() {}, "jsonp").done(function(resp) {
            var countryCode = (resp && resp.country_code) ? resp.country_code : "";
            callback(countryCode);
          }).fail(function(jqXHR) {
            console.warn('GeoIP Error: ' + jqXHR.status);
            callback(defaultCode);
          });
        }
      },
      allowDropdown: data.allowDropdown !== undefined ? true : false
    };

    options.utilsScript = 'https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/12.4.0/js/utils.js';
    options.preferredCountries = data.preferredCountries,


    $el.intlTelInput(options)
    .done(function() {
      $form = $el.closest('form');
      if (forms.indexOf($form) === -1) {
        $form.submit(function(e) {
          $realInput.val(function() {
            return $el.intlTelInput("getNumber");
          });
        });

        forms.push($form);
      }

      if ($realInput.val() !== '') {
        $el.intlTelInput('setNumber', $realInput.val());
      }
    });
  });
})(jQuery);
