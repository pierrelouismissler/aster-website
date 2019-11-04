var map;
var dark_mode_style = [
    {elementType: 'geometry', stylers: [{color: '#242f3e'}]},
    {elementType: 'labels.text.stroke', stylers: [{color: '#4f6075'}]},
    {elementType: 'labels.text.fill', stylers: [{visibility: 'off'}]},//color: '#746855'}]},
    {
        featureType: 'administrative',
        elementType: 'labels.text.fill',
        stylers: [{visibility: 'off'}]//color: '#ff006c'}]
    },
    {
        featureType: 'poi',
        elementType: 'labels',
        stylers: [{visibility: 'off'}]//color: '#d59563'}]
    },
    {
        featureType: 'poi.park',
        elementType: 'geometry',
        stylers: [{color: '#263c3f'}]
    },
    {
        featureType: 'road',
        elementType: 'geometry',
        stylers: [{color: '#38414e'}]
    },
    {
        featureType: 'road',
        elementType: 'geometry.stroke',
        stylers: [{color: '#212a37'}]
    },
    {
        featureType: 'road',
        elementType: 'labels.text.fill',
        stylers: [{color: '#9ca5b3'}]
    },
    {
        featureType: 'road.highway',
        elementType: 'geometry',
        stylers: [{color: '#ff006c'}]
    },
    {
        featureType: 'road.highway',
        elementType: 'geometry.stroke',
        stylers: [{color: '#1f2835'}]
    },
    {
        featureType: 'road.highway',
        elementType: 'labels',
        stylers: [{visibility: 'off'}]//color: '#ff365e'}]
    },
    {
        featureType: 'transit',
        elementType: 'labels',
        stylers: [{visibility: 'off'}]//'#2f3948'}]
    },
    {
        featureType: 'water',
        elementType: 'geometry',
        stylers: [{color: '#17263c'}]
    },
    {
        featureType: 'water',
        elementType: 'labels.text.fill',
        stylers: [{color: '#515c6d'}]
    },
    {
        featureType: 'water',
        elementType: 'labels.text.stroke',
        stylers: [{color: '#17263c'}]
    }
];

// Initialize and add the map
function initMap() {

    //////////////////////////  Map options  ///////////////////
    const map_options = {
        zoom: map_parameters.zoom,
        center: {lat: map_parameters.lat, lng: map_parameters.lng},
        mapTypeId: map_parameters.mapType,
        styles: dark_mode_style,
        streetViewControl: false,
        fullscreenControl: false,
        mapTypeControl: false
    };

    map = new google.maps.Map(document.getElementById('map'), map_options);

    //////////////////////////  Center on user  ///////////////////

    // Allow the map to be centered on the user's location
    if (map_parameters.center_on_user_location) {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function(position) {
                var pos = {
                    lat: position.coords.latitude,
                    lng: position.coords.longitude
                };
                map.setCenter(pos);
            }, function() {
                handleLocationError(true, infoWindow, map.getCenter());
            });
        }
        else {
            // Browser doesn't support Geolocation
            handleLocationError(false, infoWindow, map.getCenter());
        }
    }
}

document.getElementById('close-demo').addEventListener('click', function(event){

    function update_markers(last_response) {

        // Scrape parameters
        var latitude = parseFloat(last_response.latitude);
        var longitude = parseFloat(last_response.longitude);
        var score = parseFloat(last_response.priority).toFixed(2);
        var phone_number = last_response.phone_number;

        // Defines markers
        var marker = new google.maps.Marker({
            position: new google.maps.LatLng(latitude, longitude),
            title: phone_number,
            map: map
        });

        // Defines the info window
        var contentString = '<div id="content"><div id="siteNotice"></div>'+
            '<div id="bodyContent" style="color: #1b1e21"><p><strong>Phone number:</strong> ' + phone_number + '</p>' +
            '<p><strong>Priority:</strong> ' + score.toString() + '</p></div></div>';

        var infowindow = new google.maps.InfoWindow({
            content: contentString
        });

        // Links the info window with the marker
        marker.addListener('click', function () {
            infowindow.open(map, marker);
        });
    }

    update_markers(last_response);

}, false);

function handleLocationError(browserHasGeolocation, infoWindow, pos) {
    infoWindow.setPosition(pos);
    infoWindow.setContent(browserHasGeolocation ?
        'Error: The Geolocation service failed.' :
        'Error: Your browser doesn\'t support geolocation.');
    infoWindow.open(map);
}
