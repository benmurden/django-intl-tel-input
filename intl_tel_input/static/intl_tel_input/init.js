(function($) {
  var $el, $realInput, options, $form, data, defaultCode,
      cssClass = '.js-intl-tel-input',
      hiddenCssClass = '.js-intl-tel-input-hidden',
      forms = [],
      inputs = $(cssClass);

  inputs.each(function(i, el) {
    $el = $(el);
    $realInput = $el.siblings(hiddenCssClass);
    data = $el.data();
    defaultCode = data.defaultCode !== undefined ? data.defaultCode : 'us';
    options = {
      initialCountry: data.autoGeoIp ? 'auto' : data.defaultCode,
      geoIpLookup: function(callback) {
        if (data.autoGeoIp) {
          $.get('https://freegeoip.net/json/', function() {}, "jsonp").done(function(resp) {
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

    options.utilsScript = 'https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/11.1.1/js/utils.js';

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
