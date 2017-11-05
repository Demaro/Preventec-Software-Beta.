let table = $('#checkAll').DataTable({
    // "processing": true,
    // "serverSide": true,
    "ajax": {
        "url": "/api/music/",
        "type": "GET",
        "dataSrc":""
    },
    "columns": [
        {"data": "nombre"},
        {"data": "porcent %"},
        {"data": "estado"},
        {"data": "responsable"},
        {"data": "fecha_inicio"},
        {"data": "fecha_termino"},
        {
            "data": null,
            "defaultContent": '<button type="button" class="btn btn-info">Edit</button>' + '&nbsp;&nbsp' +
            '<button type="button" class="btn btn-danger">Delete</button>'
        }
    ]
});

let id = 0;

$('#checkAll tbody').on('click', 'button', function () {
    let data = table.row($(this).parents('tr')).data();
    let class_name = $(this).attr('class');
    if (class_name == 'btn btn-info') {
        // EDIT button
        $('#responsable').val(data['responsable']);
        $('#fecha_inicio').val(data['fecha_inicio']);
        $('#fecha_termino').val(data['fecha_termino']);
        $('#type').val('edit');
        $('#modal_title').text('EDIT');
        $("#myModal0").modal();
    } else {
        // DELETE button
        $('#modal_title').text('DELETE');
        $("#confirm").modal();
    }

    id = data['id'];

});

$('form').on('submit', function (e) {
    e.preventDefault();
    let $this = $(this);
    let type = $('#type').val();
    let method = '';
    let url = '/api/carpeta/';
    if (type == 'new') {
        // new
        method = 'POST';
    } else {
        // edit
        url = url + id + '/';
        method = 'PUT';
    }

    $.ajax({
        url: url,
        method: method,
        data: $this.serialize()
    }).success(function (data, textStatus, jqXHR) {
        location.reload();
    }).error(function (jqXHR, textStatus, errorThrown) {
        console.log(jqXHR)
    });
});

$('#confirm').on('click', '#delete', function (e) {
    $.ajax({
        url: '/api/carpeta/' + id + '/',
        method: 'DELETE'
    }).success(function (data, textStatus, jqXHR) {
        location.reload();
    }).error(function (jqXHR, textStatus, errorThrown) {
        console.log(jqXHR)
    });
});


$('#new').on('click', function (e) {
    $('#responsable').val('');
    $('#fecha_inicio').val('');
    $('#fecha_termino').val('');
    $('#type').val('new');
    $('#modal_title').text('NEW');
    $("#myModal0").modal();
});



