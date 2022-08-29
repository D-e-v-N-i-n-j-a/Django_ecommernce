
const data = []
const product = document.querySelectorAll('.ti-shopping-cart');
product.forEach((btn)=>{
    btn.addEventListener('click',(event)=>{
        const product_id = event.target.parentElement.dataset.product;
        const img = event.target.parentElement.parentElement.parentElement.children[0].src
        const price = event.target.parentElement
        data.push(product_id,img,price)
         
    });
})