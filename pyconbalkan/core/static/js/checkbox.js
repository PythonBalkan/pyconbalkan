window.onload = toggleSelect(); // to disable select on load if needed

function toggleSelect()
{
    var number_of_tickets = document.getElementById("id_no_tickets").value * 25;
    var airport_transport = document.getElementById("id_airport").value;
    var airport_transport_value = 0;
    if(airport_transport === 'yes')
    {
        airport_transport_value = 15;
    }
    var total = number_of_tickets + airport_transport_value;


    var checkbox = document.getElementById("id_book_hotel").checked;
    var label1 = document.getElementById("id_no_person_label");
    var label2 = document.getElementById("id_no_nights_label");

    document.getElementById("id_no_person").disabled = !checkbox;
    document.getElementById("id_no_nights").disabled = !checkbox;
    if(checkbox)
    {
        label1.classList.add('font400');
        label1.classList.add('font-blue');
        label1.classList.remove('font-grey');
        label2.classList.add('font400');
        label2.classList.add('font-blue');
        label2.classList.remove('font-grey');
        var book_hotel = document.getElementById("id_no_person").value * 110;
        total += book_hotel;
    }

    if(!checkbox)
    {
        label1.classList.remove('font-blue');
        label1.classList.add('font-grey');
        label2.classList.remove('font-blue');
        label2.classList.add('font-grey');
    }


    total += 25; //lunch
    $('#total').html(total)

}