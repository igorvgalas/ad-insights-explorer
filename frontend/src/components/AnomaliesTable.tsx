import React, { useMemo, useState } from "react";
import { useAnomalies } from "../hooks/useAnomalies";
import CustomTable from "./CustomTable";
import { Input, Box } from "@chakra-ui/react";

interface Anomaly {
  userId: number;
  id: number;
  title: string;
  reason: string;
}

const AnomaliesTable = () => {
  const { data: anomalies, isLoading, isError } = useAnomalies();
  const [filterUserId, setFilterUserId] = useState("");

  const filteredData = useMemo(() => {
    if (!filterUserId) return anomalies || [];
    return (anomalies || []).filter((anomaly: Anomaly) =>
      anomaly.userId.toString().includes(filterUserId)
    );
  }, [anomalies, filterUserId]);

  const columns = useMemo(
    () => [
      {
        header: "User ID",
        accessorKey: "userId",
      },
      {
        header: "ID",
        accessorKey: "id",
      },
      {
        header: "Title",
        accessorKey: "title",
      },
      {
        header: "Reason",
        accessorKey: "reason",
      },
    ],
    []
  );

  if (isLoading) return <div>Loading...</div>;
  if (isError || !anomalies) return <div>Error loading anomalies data.</div>;

  return (
    <>
      <Input
        placeholder="Filter by User ID"
        value={filterUserId}
        onChange={(e) => setFilterUserId(e.target.value)}
        mb={4}
      />
      <Box borderWidth="1px" borderRadius="lg" p={4} textAlign="center">
        <CustomTable data={filteredData} columns={columns} />
      </Box>
    </>
  );
};

export default AnomaliesTable;
