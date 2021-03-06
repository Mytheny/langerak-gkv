$(function() {

	// should get this from the settings but meh
	FOOTER_MAP_COORDINATES = {
		lat: 51.9307267,
		lng: 4.8763104
	};

	$(window).on('map:init', function (e) {
		var detail = e.originalEvent ? e.originalEvent.detail : e.detail;
		// add marker
		// console.log(detail.map);
		L.marker([FOOTER_MAP_COORDINATES.lat, FOOTER_MAP_COORDINATES.lng]).addTo(detail.map);
	});

	$(window).resize(function() {
	    $('.link-height').data('processed', false).height('auto');
	    syncHeights();
	});

    $('.help').popover({
        'placement': 'auto right'
    });

    $('form.dropdown-menu').click(function(e) {
        e.preventDefault();
        return false;
    });
});

$(window).load(syncHeights);


function syncHeights() {
    $('.link-height').each(function() {
        if($(this).data('processed')) {
            return;
        }

        var linkID = $(this).data('linkid');
        var set  = $('.link-height[data-linkid="'+linkID+'"]');
        set.data('processed', true);

        var height = $.map(set, function(e) {
            return $(e).height();
        }).reduce(function(prevResult, element, index, input) {
            return Math.max(prevResult, element);
        });
        set.each(function() {
            $(this).height(height);
        });
    });
}
