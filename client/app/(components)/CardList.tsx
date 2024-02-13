"use client"
import CardItem from "./CardItem"

const CardList = ({products}) => {
    const displayProducts = products?.map((product) => {
        return <CardItem description = {product.description} name = {product.name} price = {product.price} image = {product.image}/>
    })
    return (
        <div>
            {displayProducts}
        </div>
    )

}

export default CardList