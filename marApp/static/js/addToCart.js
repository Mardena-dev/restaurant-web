const product = [
    {
        id: 0,
        image: 'sa1.jpg',
        title: 'Black rice salad',
        price: 7,
    },
    {
        id: 1,
        image: 'sa2.jpg',
        title: 'Cucumber and peach salad',
        price: 7,
    },
    {
        id: 2,
        image: 'sa4.jpg',
        title: 'Kale and radicchio quinoa salad',
        price: 7,
    },
    {
        id: 3,
        image: 'sa5.jpg',
        title: 'Octopus salad',
        price: 7,
    },


    {
        id: 4,
        image: 'su6.jpg',
        title: 'Sweet potato soup',
        price: 10,
    },
    {
        id: 5,
        image: 'su1.jpg',
        title: 'French onion soup',
        price: 10,
    },
    {
        id: 6,
        image: 'su3.jpg',
        title: 'Nettle soup',
        price: 10,
    },
    {
        id: 7,
        image: 'su4.jpg',
        title: 'Tomato soup',
        price: 10,
    },

    {
        id: 8,
        image: 'p1.jpg',
        title: 'Butter-roasted tomato buccatini',
        price: 13,
    },
    {
        id: 9,
        image: 'p5.jpg',
        title: 'Fetttuccine alfredo with asparagus',
        price: 13,
    },
    {
        id: 10,
        image: 'p8.jpg',
        title: 'Prawn linguine',
        price: 13,
    },
    {
        id: 11,
        image: 'p9.jpg',
        title: 'Penne alla vodka',
        price: 13,
    },

    {
        id: 12,
        image: 'm1.jpg',
        title: 'Beef short ribs with pumpkin',
        price: 21,
    },
    {
        id: 13,
        image: 'm2.jpg',
        title: 'Wagyu with parsnip puree',
        price: 21,
    },
    {
        id: 14,
        image: 'm3.jpg',
        title: 'Pistachio crusted lamb rack',
        price: 21,
    },
    {
        id: 15,
        image: 'm4.jpg',
        title: 'Roasted chicken breast',
        price: 21,
    },

    {
        id: 16,
        image: 'd1.jpg',
        title: 'Grilled octopus, squid ink pasta',
        price: 25,
    },
    {
        id: 17,
        image: 'd2.jpg',
        title: 'Mussels in dry sherry',
        price: 25,
    },

    {
        id: 18,
        image: 'e3.jpg',
        title: 'Mushroom truffle custard',
        price: 9,
    },
    {
        id: 19,
        image: 'e4.jpg',
        title: 'Souffle',
        price: 9,
    },
];
const categories = [... new Set(product.map((item) => { return item }))]
let i = 0;
document.getElementById('root').innerHTML = categories.map((item) => {
    var { image, title, price } = item;
    return (
        `<div class='box' >
    <div class='img-box' >
    <img class='images' src=/static/images/${image}></img>
    </div>
    <div class='bottom'>
    <p>${title}</p>
    <h2>$ ${price}.00</h2>` +
        "<button onclick='addtocart(" + (i++) + ")'>Add to cart</button>" +
        `</div>
    </div>`
    )
}).join('')


var cart = [];

function addtocart(a) {
    cart.push({ ...categories[a] });
    displayCart();
}

function delElement(a) {
    cart.splice(a, 1);
    displayCart();
}

function displayCart(a) {
    let total = 0;
    let j = 0;
    document.getElementById('count').innerHTML = cart.length;
    if (cart.length == 0) {
        document.getElementById('cartItem').innerHTML = "No order yet";
        document.getElementById("total").innerHTML = "$" + total + ".00";
    }
    else {
        document.getElementById("cartItem").innerHTML = cart.map((items) => {
            var { image, title, price } = items;
            total = total + price;
            document.getElementById("total").innerHTML = "$" + total + ".00";
            return (
                `<div class='cart-item'>
                    <div class='row-img'>
                        <img class='rowimg' src=/static/images/${image}>
                        </div>
                        <p style='font-size:12px'>${title}</p>
                        <h2 style='font-size: 15px;'>${price}.00</h2>` +
                "<i class='fa-solid fa-trash' onclick='delElement(" + (j++) + ")'></i></div>"
            );
        }).join('');
    }
}