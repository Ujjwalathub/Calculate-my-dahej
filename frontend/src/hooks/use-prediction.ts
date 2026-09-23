import { useMutation, useQuery } from "@tanstack/react-query";
import { api, type DowryData, type StartupData, type PredictionResponse } from "@/lib/api";

/**
 * Hook for making single predictions
 */
export function usePrediction() {
  return useMutation<PredictionResponse, Error, DowryData | StartupData>({
    mutationFn: (data: DowryData | StartupData) => api.predictSingle(data),
  });
}

/**
 * Hook for batch predictions
 */
export function useBatchPrediction() {
  return useMutation({
    mutationFn: (items: (DowryData | StartupData)[]) => api.predictBatch(items),
  });
}

/**
 * Hook for fetching model info
 */
export function useModelInfo() {
  return useQuery({
    queryKey: ["modelInfo"],
    queryFn: () => api.getModelInfo(),
    staleTime: 1000 * 60 * 5, // 5 minutes
  });
}

/**
 * Hook for checking API health
 */
export function useApiHealth() {
  return useQuery({
    queryKey: ["apiHealth"],
    queryFn: () => api.health(),
    refetchInterval: 30000, // Refetch every 30 seconds
    retry: 1,
  });
}
