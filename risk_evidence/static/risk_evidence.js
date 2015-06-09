jQuery(document).ready(function(){
    $('#table1 td.y_n').each(function(){
        if ($(this).text() == 'NA') {
            $(this).css('color', '#F0F0F5');
        }
        if ($(this).text() == 'N') {
            $(this).css('background-color', '#B8D08A');
        }
        if ($(this).text() == 'C') {
            $(this).css('background-color', '#B9CFED');
        }
        if ($(this).text() == 'C C') {
            $(this).css('background-color', '#4377CC');
        }
        if ($(this).text() == 'I') {
            $(this).css('background-color', '#FBE4D0');
        }
        if ($(this).text() == 'I I') {
            $(this).css('background-color', '#D9550C');
        }
    });

    $('#table3 td.y_n').each(function(){
        if ($(this).text() == 'High') {
            $(this).css('color','#3FA53E');
        }
        if ($(this).text() == 'Medium') {
            $(this).css('color','#FDB430');
        }
        if ($(this).text() == 'Low') {
            $(this).css('color','#880046');
        }
    });
});

