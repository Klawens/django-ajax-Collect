function add_fav(current_elem, fav_id, fav_type, csrf){
    $.ajax({
        cache: false,
        type: "POST",
        url:"/community/fav/",//此处为自己配置的urls
        data:{'fav_id':fav_id, 'fav_type':fav_type},//对应数据表的字段
        async: true,
        beforeSend:function(xhr, settings){
            xhr.setRequestHeader("X-CSRFToken", csrf);
        },
        success: function(data) {
            if(data.status == 'fail'){
                if(data.msg == '未登录'){
                    window.location.href = '/login/';
                    //如果未登录就跳转至登录界面
                }else{
                    current_elem.html(data.msg)
                    //将收藏状态写入按钮
                }

            }else if(data.status == 'success'){
                current_elem.html(data.msg)
                //将收藏状态写入按钮
            }
        },
    });
}