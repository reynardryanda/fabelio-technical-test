import React from 'react';
import styled from 'styled-components';

const Product = ({ product }) => {
  const Container = styled.div`
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;

    @media only screen and (max-width: 1110px) {
      flex-direction: column;
      margin-top: 3.825rem;
      height: 100%;
    }

    @media only screen and (max-width: 420px) {
      margin-top: 3.2rem;
    }
  `;

  const FlexWrapper = styled.div`
    display: flex;
    justify-content: center;
    align-items: center;
  `;

  const ImageWrapper = styled.div`
    max-width: 100%;
    border-radius: 20px;
    margin: auto;
    padding: 0rem 2rem;
    bottom: 0;

    @media only screen and (max-width: 1110px) {
      padding: 0;
      max-width: 100%;
      border-radius: 0;
    }
  `;

  const Image = styled.img`
    width: 100%;
    border-radius: 20px;
    box-shadow: 0px 10px 10px rgba(0, 0, 0, 0.25);
    @media only screen and (max-width: 1110px) {
      border-radius: 0;
      box-shadow: none;
    }
  `;

  const BackgroundWhite = styled.div`
    background-color: white;
    height: 100%;
  `;

  const Description = styled.div`
    height: 100%;
    background: #fce38a;
    display: flex;
    justify-content: center;
    align-items: flex-start;
    flex-direction: column;
    padding: 0rem 10rem;

    @media only screen and (max-width: 1310px) {
      padding: 4rem 2rem 2rem 2rem;
    }
  `;

  const Title = styled.p`
    font-size: 3rem;
  `;

  const Price = styled.p`
    font-size: 2.5rem;
    font-weight: 300;
  `;

  const Details = styled.p`
    padding: 3rem 0rem;
    font-size: 2rem;
    font-weight: 300;
  `;

  const Button = styled.button`
    letter-spacing: 2px;
    padding: 1rem 1.5rem;
    font-size: 1rem;
    background-color: #3e3f43;
    font-weight: 300;
    color: #fff;
    border: none;
    outline: none;
    cursor: pointer;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.15);
  `;

  const color = product.details.map((detail,index) => {
    if (product.details.length-1 == index) {
      return `dan ${detail.color}`
    } else {
      return `${detail.color}, `
    }
  })

  return (
    <Container>
      <ImageWrapper>
        <Image src={product.image_url} alt={product.name} />
      </ImageWrapper>
      <BackgroundWhite>
        <Description>
          <Title>{product.name}</Title>
          <Price>Rp{String(product.price).split(/(?=(?:...)*$)/).join('.')},00</Price>
          <Details>
            Sofa {product.max_seats} dudukan dengan dimensi {product.dimension} dan terbuat dari {product.material} tersedia dalam {product.details.length} warna, {color}.
          </Details>
          <Button>Beli Sekarang</Button>
        </Description>
      </BackgroundWhite>
    </Container>
  );
};

export default Product;
