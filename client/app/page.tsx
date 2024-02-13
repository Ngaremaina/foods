"use client"
import CardList from "./(components)/CardList";
import { useEffect, useState } from "react";

export default function Home() {
  const [products, setProducts] = useState([])

  useEffect(() => {
    const fetching = async () => {
      const response = await fetch("")
      const data = await response.json()
      return setProducts(data)
    }
    fetching()
  },[])
  
  return (
    <div>
      <CardList products = {products}/>
      
    </div>
   
  );
}
