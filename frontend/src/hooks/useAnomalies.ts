import { useQuery } from '@tanstack/react-query';
import { fetchAnomalies } from '../services/api';

export const useAnomalies = () => {
  return useQuery({
    queryKey: ['anomalies'],
    queryFn: fetchAnomalies,
  });
};

