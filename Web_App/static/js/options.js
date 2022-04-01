let cities = new Array('İstanbul', 'Ankara', 'Diyarbakır', 'Tokat', 'Gaziantep',
    'Afyonkarahisar', 'Edirne', 'Kocaeli', 'Bursa', 'İzmir', 'Sakarya',
    'Elazığ', 'Kayseri', 'Eskişehir', 'Şanlıurfa', 'Samsun', 'Adana',
    'Antalya', 'Kastamonu', 'Uşak', 'Muğla', 'Kırklareli', 'Konya',
    'Karabük', 'Tekirdağ', 'Denizli', 'Balıkesir', 'Aydın', 'Amasya',
    'Kütahya', 'Bolu', 'Trabzon', 'Isparta', 'Osmaniye');

const showCities = (target_id) => {
    let option_str = document.getElementById(target_id);
    option_str.length = 0;
    option_str.options[0] = new Option('Select City', '');
    option_str.selectedIndex = 0;
    for (var i = 0; i < cities.length; i++) {
        option_str.options[option_str.length] = new Option(cities[i], cities[i]);
    }
}

let resTypes = new Array('Food Court', 'In line', 'Mobile', 'Drive Thru');

const showResTyps = (target_id) => {
    let option_str = document.getElementById(target_id);
    option_str.length = 0;
    option_str.options[0] = new Option('Select Restaurant type', '');
    option_str.selectedIndex = 0;
    for (var i = 0; i < resTypes.length; i++) {
        option_str.options[option_str.length] = new Option(resTypes[i], resTypes[i]);
    }
}