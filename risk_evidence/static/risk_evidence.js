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

$("#id_form1-evidence").on("keyup paste", function() {
    $("#id_form2-evidence").val($(this).val());
});
$("#id_form1-summary").on("keyup paste", function() {
    $("#id_form2-summary").val($(this).val());
});
$("#id_form1-source").on("keyup paste", function() {
    $("#id_form2-source").val($(this).val());
});
$("#id_form1-type").on("keyup paste", function() {
    $("#id_form2-type").val($(this).val());
});

//$('#right').find(".form-country").on('change',function(){
//    $('#id_summary').val("hahah");
//
//});

jQuery(document).ready(function () {
    $('.form-control2').on('click', function() {
        $('.errorlist').hide();
    });
    $('.form-control3').on('click', function() {
        $('.errorlist').hide();
    });
});

function sync(el1, el2) {
    if (!el1) {
        return false;
    }
    else {
        var val = el1.value;
        var syncWith = document.getElementById(el2);
        var options = syncWith.getElementsByTagName('option');
        for (var i = 0, len = options.length; i < len; i++) {
            if (options[i].value == val) {
                options[i].selected = true;
            }
        }
    }
}

var selectToSync = document.getElementById('id_form1-country');
selectToSync.onchange = function(){
    sync(this,'id_form2-country');
};

var selectToSync2 = document.getElementById('id_form2-country');
selectToSync2.onchange = function(){
    sync(this,'id_form1-country');
};


