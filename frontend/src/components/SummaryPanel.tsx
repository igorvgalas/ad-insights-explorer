import React, { useMemo } from "react";
import { useSummary } from "../hooks/useSummary";
import CustomTable from "./CustomTable";
import {
  Box,
  Heading,
  Spinner,
  Alert,
  AlertIcon,
  VStack,
  Tag,
  Wrap,
  WrapItem,
} from "@chakra-ui/react";

type TopUser = {
  userId: number;
  uniqueWords: number;
};

type CommonWord = {
  word: string;
  count: number;
};

type SummaryData = {
  topUsers: TopUser[];
  commonWords: [string, number][];
};

const SummaryPanel = () => {
  const { data, isLoading, isError } = useSummary();

  const summary = data as SummaryData | undefined;

  const topUsersColumns = useMemo(
    () => [
      {
        header: "User ID",
        accessorKey: "userId",
      },
      {
        header: "Unique Words",
        accessorKey: "uniqueWords",
      },
    ],
    []
  );

  const transformedCommonWords = useMemo(
    () =>
      summary?.commonWords.map(([word, count]) => ({
        word,
        count,
      })) || [],
    [summary]
  );

  if (isLoading)
    return (
      <Box textAlign="center" py={10} px={6}>
        <Spinner size="xl" />
      </Box>
    );

  if (isError || !summary)
    return (
      <Alert status="error" borderRadius="md">
        <AlertIcon />
        Error loading summary data.
      </Alert>
    );

  return (
    <VStack spacing={8} align="stretch">
      <Box borderWidth="1px" borderRadius="lg" p={4} textAlign="center">
        <Box w={"60%"} justifyContent={"center"} mx="auto">
          <Heading as="h2" size="lg" mb={4}>
            Top 3 Users
          </Heading>
          <CustomTable data={summary.topUsers} columns={topUsersColumns} />
        </Box>
      </Box>

      <Box borderWidth="1px" borderRadius="lg" p={4} textAlign="center">
        <Heading as="h2" size="lg" mb={4}>
          Most Common Words
        </Heading>
        <Wrap mt={4} justify="center">
          {transformedCommonWords.map((word) => (
            <WrapItem key={word.word}>
              <Tag size="lg" colorScheme="teal">
                {word.word} ({word.count})
              </Tag>
            </WrapItem>
          ))}
        </Wrap>
      </Box>
    </VStack>
  );
};

export default SummaryPanel;
