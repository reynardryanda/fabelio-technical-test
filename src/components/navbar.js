import React from "react"
import styled from "styled-components"

const Navbar = (props) => {

    const Navbar = styled.nav`
        position: fixed;
        display: flex;
        justify-content: flex-start;
        align-items: center;
        width: 100vw;
        top:0;
        @media only screen and (max-width: 1110px) {
            background-color: #F3F3F3;
            box-shadow: 0px 2px 2px rgba(0, 0, 0, 0.15);
          }
    `

    const Logo = styled.div`
        padding: 1rem
        cursor: pointer;
    `

    const LogoText = styled.p`
        font-size: 2rem;
        line-height: 0;
    `

    const NavLinks = styled.div`
        display: flex;
        justify-content: center;
        align-items: center;
        margin-left: 1rem;
        font-size: 1.5rem;
    `

    const Link = styled.div`
        padding: 1rem;
        cursor: pointer;
    `

    return (
        <Navbar>
            <Logo>
                <LogoText>REYNARD</LogoText>
            </Logo>
            <NavLinks>
                <Link>
                    <p>Sofa</p>
                </Link>
                <Link>
                    <p>Meja</p>
                </Link>
                <Link>
                    <p>Kursi</p>
                </Link>
            </NavLinks>
        </Navbar>
    )
}

export default Navbar