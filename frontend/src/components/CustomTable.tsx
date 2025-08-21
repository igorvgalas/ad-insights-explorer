import React, { useMemo } from "react";
import {
  Table,
  Thead,
  Tbody,
  Tr,
  Th,
  Td,
  TableContainer,
  Text,
  Flex,
  useColorModeValue,
} from "@chakra-ui/react";
import { FaSortDown, FaSortUp } from "react-icons/fa";
import {
  useReactTable,
  getCoreRowModel,
  getSortedRowModel,
  ColumnDef,
  SortingState,
} from "@tanstack/react-table";

interface CustomTableProps<T> {
  data: T[];
  columns: ColumnDef<T>[];
}

const CustomTable = <T extends object>({
  data,
  columns,
}: CustomTableProps<T>) => {
  const [sorting, setSorting] = React.useState<SortingState>([]);

  const table = useReactTable({
    data,
    columns,
    state: { sorting },
    onSortingChange: setSorting,
    getCoreRowModel: getCoreRowModel(),
    getSortedRowModel: getSortedRowModel(),
  });

  const iconColor = useColorModeValue("black", "white");

  return (
    <TableContainer>
      <Table variant="simple">
        <Thead>
          {table.getHeaderGroups().map((headerGroup) => (
            <Tr key={headerGroup.id}>
              {headerGroup.headers.map((header) => (
                <Th
                  key={header.id}
                  onClick={header.column.getToggleSortingHandler()}
                >
                  <Flex justifyContent="space-between" alignItems="center">
                    <Text>
                      {header.isPlaceholder
                        ? null
                        : typeof header.column.columnDef.header === "function"
                        ? header.column.columnDef.header(header.getContext())
                        : header.column.columnDef.header}
                    </Text>
                    {header.column.getCanSort() && (
                      <Flex direction="column" ml={2} alignItems="center">
                        {header.column.getIsSorted() === "asc" && (
                          <FaSortUp style={{ color: iconColor }} />
                        )}
                        {header.column.getIsSorted() === "desc" && (
                          <FaSortDown style={{ color: iconColor }} />
                        )}
                      </Flex>
                    )}
                  </Flex>
                </Th>
              ))}
            </Tr>
          ))}
        </Thead>
        <Tbody>
          {table.getRowModel().rows.map((row) => (
            <Tr key={row.id}>
              {row.getVisibleCells().map((cell) => (
                <Td key={cell.id}>
                  {typeof cell.column.columnDef.cell === "function"
                    ? cell.column.columnDef.cell(cell.getContext())
                    : cell.column.columnDef.cell}
                </Td>
              ))}
            </Tr>
          ))}
        </Tbody>
      </Table>
    </TableContainer>
  );
};

export default CustomTable;
