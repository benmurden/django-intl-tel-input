(function($) {
  var $el, options,
      inputs = $('.intl-tel-input');

  inputs.forEach(function(i, el) {
    $el = $(el);
    options = {};

    if ($el.attr('data-utils-script')) {
      options['utilsScript'] = 'https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/9.0.1/js/utils.js';
    }

    $el.intlTelInput(options);
  });
})(jQuery);
