$(document).ready(function() {

    $('#super').on('click', function (e) {
        load(e);
    });

    // Input press "enter" submit
    $('#searchInput').on('keyup', function (e) {
        if (e.keyCode === 13) {
            load(e);
        };
    });

    // Add to cart button
    let elements1 = document.getElementsByClassName("btn cart px-auto");
    Array.from(elements1).forEach(function(element) {
        element.addEventListener('click', addToCart);
    });

    // filter superclass options
    $('#selectValue').on('change', function (e) {
        selectOption(e)
    });

    //username availability
    $('#checkUsername').on('click', function(e) {
        checkUsername(e);
    });
});

let cartQuant = 0;

if(document.getElementById('cartQuantity') === null || document.getElementById('cartQuantity') === undefined){
    cartQuant = 0;
}
else {
    cartQuant = document.getElementById('cartQuantity').innerHTML;
};

function checkUsername(e){
    let username = document.getElementById("usernameInput").value
    e.preventDefault();
    $.ajax( {
        url: '/user/names',
        type: 'GET',
        success: function(res) {
            let newdata = 0
            res.data.map(d => {
                if(username == d.username){
                    $('#usernameInput').removeClass('input100');
                    $('#usernameInput').removeClass('input102');
                    $('#usernameInput').addClass('input101');
                    newdata++
                }
            });
            if (newdata == 0) {
                $('#usernameInput').removeClass('input100');
                $('#usernameInput').removeClass('input101');
                $('#usernameInput').addClass('input102');
            }
        },
        error: function(xhr, status, error) {
            console.error(error)
        }
    })
}


function selectOption(e){
    let selectVal = document.getElementById("selectValue").value;
    e.preventDefault();
    $.ajax( {
        url: '/products/class/' + selectVal,
        type: 'GET',
        success: function(res) {
            let newHtml = res.data.map(d => {
                return `<option value="${d.subclass}">${d.subclass}</option>`
            });
            newHtml.unshift('<option value disabled selected />--select--</option>')
            $('#selectSubclass').html(newHtml.join(''));
        },
        error: function(xhr, status, error) {
            console.error(error)
        }
    })
};

function load(e){
    e.preventDefault();
       let searchText = $('#searchInput').val();
       $.ajax( {
           url: '/products?searchFilter=' + searchText,
           type: 'GET',
           success: function(res) {
               let newHtml = res.data.map(d => {
                   return `<div class="product1">
                                <a href="/products/${d.id}">
                                    <img class="pimg" src="${d.image}"/>
                                    <h4>${d.name}</h4>
                                    <p>${d.price}</p>
                                </a>
                            </div>`
               });
               $('.products').html(newHtml.join(''));
           },
           error: function(xhr, status, error) {
               // TODO: show toastr
               console.error(error)
           }
       })
};

// ADD TO CART
function addToCart(e) {
    e.preventDefault();
    $.ajax({
        url : "/products/",
        type: "POST",
        data : {csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value, id: this.parentElement.children[1].value},
        dataType : "json",
        success: function( data ){
            // test
        }
    });
    cartQuant++;
    console.log("value of cart add: " + cartQuant)
    document.getElementById('cartQuantity').innerHTML = cartQuant
};

