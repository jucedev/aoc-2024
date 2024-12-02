namespace _2nd;

internal static class Program
{
    public static void Main(string[] args)
    {
        var report = File.ReadAllLines("input.txt").ToList();
        var strictScore = CalculateSafety(report, false);
        var looseScore = CalculateSafety(report, true);
        Console.WriteLine($"Strict Score: {strictScore}");
        Console.WriteLine($"Loose Score: {looseScore}");
    }

    private static int CalculateSafety(List<string> input, bool validateLoosely)
    {
        return input
            .Select(line => line.Split(" ").Select(int.Parse).ToList())
            .Sum(validateLoosely ? LooselyValidate : Validate);
    }

    private static int LooselyValidate(List<int> levels)
    {
        if (Validate(levels) == 1) return 1;
        
        return levels
            .Select((_, i) => levels.Take(i).Concat(levels.Skip(i + 1)).ToList())
            .Any(reducedList => Validate(reducedList) == 1) ? 1 : 0;
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














