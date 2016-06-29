(function($) {
  var $el, options,
      inputs = $('.intl-tel-input');

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

    $el.intlTelInput(options);
  });
})(jQuery);
