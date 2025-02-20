import {
  Container,
  Accordion,
  AccordionDetails,
  AccordionSummary,
  CircularProgress,
  Typography,
  Link,
} from "@mui/material";
import { ProductsTable } from "../ProductsTable/ProductsTable";
import "./ProductResult.css";
import LinkIcon from "@mui/icons-material/Link";

export const ProductResult = ({ products, isLoading, searchQuery }) => {
  return (
    <Container
      className="search-result"
      display={products ? "flex" : "none"}
      alignItems="center"
    >
      {isLoading ? (
        <Container
          className="loading-bar"
          style={{
            display: "flex",
            justifyContent: "center",
            alignItems: "center",
          }}
        >
          <CircularProgress sx={{ color: "#1f2937", margin: "auto" }} />
        </Container>
      ) : products && Object.entries(products).length > 0 ? (
        <div className="search-table">
          <h3 style={{ textAlign: "center" }}>
            Search Results for {searchQuery}
          </h3>
          {Object.entries(products).map(([siteName, siteData]) => (
            <Accordion key={siteName}>
              <AccordionSummary sx={{ color: "#11243d" }}>
                <Typography>
                  <a
                    href={siteData.websiteLink}
                    target="_blank"
                    rel="noopener noreferrer"
                    sx={{ color: "#003366" }}
                  >
                    {" "}
                    <LinkIcon />
                    {siteData.products.length} products found from {siteName}{" "}
                  </a>
                </Typography>
              </AccordionSummary>
              <AccordionDetails>
                <ProductsTable products={siteData.products}></ProductsTable>
              </AccordionDetails>
            </Accordion>
          ))}
        </div>
      ) : (
        <div></div>
      )}
    </Container>
  );
};
