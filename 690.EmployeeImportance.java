import java.util.stream.Collectors;

/*
// Employee info
class Employee {
    // It's the unique id of each node;
    // unique id of this employee
    public int id;
    // the importance value of this employee
    public int importance;
    // the id of direct subordinates
    public List<Integer> subordinates;
};
*/
class Solution {
    int result = 0;

    public int getImportance(List<Employee> employees, int id) {
        Employee manager = employees
            .stream()
            .filter(e -> e.id == id)
            .collect(Collectors.toList())
            .get(0);
        result += manager.importance;
        manager.subordinates.forEach(subId -> getImportance(employees, subId));
        return result;
    }
}
