import {
  Container,
  Accordion,
  AccordionDetails,
  AccordionSummary,
  CircularProgress,
  Typography,
} from "@mui/material";
import { ProductsTable } from "../ProductsTable/ProductsTable";

export const ProductResult = ({ products, isLoading }) => {
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
          <CircularProgress sx={{ color: "#f08080", margin: "auto" }} />
        </Container>
      ) : products && Object.entries(products).length > 0 ? (
        <div className="search-table">
          {Object.entries(products).map(([siteName, siteData]) => (
            <Accordion key={siteName}>
              <AccordionSummary>
                <Typography>
                  {siteData.length} products found from {siteName}
                </Typography>
              </AccordionSummary>
              <AccordionDetails>
                <ProductsTable products={siteData}></ProductsTable>
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
