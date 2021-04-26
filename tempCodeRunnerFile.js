    const leftDiff = Math.abs(keypad[left + ''][0] - keypad[num + ''][0]) + Math.abs(keypad[left + ''][1] - keypad[num + ''][1]);
    const rightDiff = Math.abs(keypad[right + ''][0] - keypad[num + ''][0]) + Math.abs(keypad[right + ''][1] - keypad[num + ''][1]);
    if (leftDiff > rightDiff) return answer += 'R';
    if (leftDiff < rightDiff) return answer += 'L'

    if (hand === 'right') return answer += 'R';
    if (hand === 'left') return answer += 'L';