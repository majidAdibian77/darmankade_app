function remove_case(case_pk) {
    $.ajax({
        type: "GET",
        url: '/remove_case',
        data: {
            "case_pk": case_pk,
        },
        dataType: "json",
        success: function (data) {
            $("#cases").load(location.href + " #cases");
        },
        failure: function () {
            alert('مشکلی به وجود آمده است!');
        }
    });
}
