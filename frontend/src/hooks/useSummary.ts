import { useQuery } from '@tanstack/react-query';
import { fetchSummary } from '../services/api';


export const useSummary = () => {
  return useQuery({
    queryKey: ['summary'],
    queryFn: fetchSummary,
  });
};
