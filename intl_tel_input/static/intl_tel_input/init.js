;(function($) {
  var options, $form, data, initialCountry, autoGeoIp, autoHideDialCode,
      cssClass = '.js-intl-tel-input',
      hiddenCssClass = '.js-intl-tel-input-hidden',
      forms = [],
      inputs = $(cssClass);

  inputs.each(function(i, el) {
    var $el = $(el);
    var $realInput = $el.siblings(hiddenCssClass);
    data = $el.data();
    initialCountry = data.initialCountry !== undefined ? data.initialCountry : '';
    autoGeoIp = data.autoGeoIp !== undefined ? true : false;
    autoHideDialCode = data.autoHideDialCode !== undefined ? true : false;

    options = {
      allowDropdown: data.allowDropdown !== undefined ? true : false,
      autoHideDialCode: autoHideDialCode,
      autoPlaceholder: data.autoPlaceholder !== undefined ? data.autoPlaceholder : 'polite',
      dropdownContainer: data.dropdownContainer !== undefined ? data.dropdownContainer : '',
      excludeCountries: data.excludeCountries !== undefined ? data.excludeCountries : [],
      formatOnDisplay: data.formatOnDisplay !== undefined ? true : false,
      geoIpLookup: function(callback) {
        if (autoGeoIp) {
          $.get('https://freegeoip.net/json/', function() {}, "jsonp").done(function(resp) {
            var countryCode = (resp && resp.country_code) ? resp.country_code : "";
            console.info('Detected country: ' + countryCode);
            callback(countryCode);
          }).fail(function(jqXHR) {
            console.warn('GeoIP Error: ' + jqXHR.status);
            callback(initialCountry);
          });
        }
      },
      initialCountry: autoGeoIp ? 'auto' : initialCountry,
      nationalMode: data.nationalMode !== undefined ? true : false,
      placeholderNumberType: data.placeholderNumberType !== undefined ? data.placeholderNumberType : 'MOBILE',
      onlyCountries: data.onlyCountries !== undefined ? data.onlyCountries : [],
      preferredCountries: data.preferredCountries !== undefined ? data.preferredCountries : ['us', 'gb'],
      separateDialCode: data.separateDialCode !== undefined ? true : false
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
