import React from 'react';
import Navbar from './navbar';
import Product from './product';
import axios from 'axios';

const HomePage = () => {
  const [product, setProduct] = React.useState({});

  React.useEffect(() => {
    let tempProducts = localStorage.getItem('products');
    if (!tempProducts) {
      axios.get('http://fabelio-technical-test.herokuapp.com//api/mst-product/').then((result) => {
        let data = result.data;
        let firstItem = data.shift();
        setProduct(firstItem);
        data.push(firstItem);
        localStorage.setItem('products', JSON.stringify(data));
      });
    } else {
      let data = JSON.parse(tempProducts);
      let firstItem = data.shift();
      setProduct(firstItem);
      data.push(firstItem);
      localStorage.setItem('products', JSON.stringify(data));
    }
  }, []);

  return (
    <>
      <Navbar />
      {product.id?<Product product={product}/>: <p>loading...</p>}
    </>
  );
};

export default HomePage;
