import React from "react";
import AnomaliesTable from "../components/AnomaliesTable";
import SummaryPanel from "../components/SummaryPanel";
import { Box, Heading, VStack, Divider, Container } from "@chakra-ui/react";

const Dashboard = () => {
  return (
    <Container maxW="container.xl" py={8}>
      <Box textAlign="center" mb={8}>
        <Heading as="h1" size="2xl" color="teal.600">
          Dashboard
        </Heading>
      </Box>
      <Box mb={8}>
        <Heading as="h2" size="lg" mb={4} color="teal.500">
          Anomalies
        </Heading>
        <AnomaliesTable />
      </Box>
      
      <Divider borderColor="gray.300" />

      <VStack spacing={10} align="stretch" mt={8}>
        <Box>
          <Heading as="h2" size="lg" mb={4} color="teal.500">
            Summary
          </Heading>
          <SummaryPanel />
        </Box>
      </VStack>
    </Container>
  );
};

export default Dashboard;
