(function($) {
  var options, data,
      cssClass = '.intl-tel-input',
      inputs = $(cssClass);

  inputs.each(function(i, el) {
    var $el;

    $el = $(el);
    data = $el.data();
    options = {
      initialCountry: data.defaultCode,
      allowDropdown: data.allowDropdown !== undefined ? true : false,
      hiddenInput: data.hiddenName
    };

    options.utilsScript = 'https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.19/js/utils.js';
    options.preferredCountries = data.preferredCountries;

    $el.intlTelInput(options);
  });
})(jQuery);
