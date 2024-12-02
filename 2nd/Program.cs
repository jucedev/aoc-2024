namespace _2nd;

internal static class Program
{
    public static void Main(string[] args)
    {
        var report = File.ReadAllLines("input.txt").ToList();
        var score = CalculateSafety(report);
        Console.WriteLine($"Safety Score: {score}");
    }

    private static int CalculateSafety(List<string> input)
    {
        return input
            .Select(line => line.Split(" ").Select(int.Parse).ToList())
            .Sum(Validate);
    }

    private static int Validate(List<int> levels)
    {
        // Less than 2 - don't think this is ever valid
        if (levels.Count < 2) return 0;

        var diffs = levels.Zip(levels.Skip(1), (a, b) => b - a).ToList();
        var increasing = diffs.All(d => d > 0);
        var decreasing = diffs.All(d => d < 0);

        if (!increasing && !decreasing) return 0;
        return diffs.All(d => Math.Abs(d) is >= 1 and <= 3) ? 1 : 0;
    }
}














