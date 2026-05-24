function generateScore(input, output) {

    const inputLength = input.length;
    const outputLength = output.length;

    const similarity =
        1 - Math.abs(inputLength - outputLength) / Math.max(inputLength, 1);

    return similarity.toFixed(4);
}


function proposeMutation(score) {

    if (score < 0.8) {
        return {
            action: "mutate_strategy",
            strategy: "reverse"
        };
    }

    return {
        action: "maintain",
        strategy: "baseline"
    };
}


function ibaValidate(proposal) {

    const forbidden = [
        "rewrite_metric",
        "rewrite_iba",
        "self_replicate"
    ];

    return !forbidden.includes(proposal.action);
}


function runCycle() {

    const input =
        document.getElementById("userInput").value;

    if (!input) {
        return;
    }

    // Runtime execution
    const output = input.toUpperCase();

    // Evaluation
    const score = generateScore(input, output);

    // Mutation proposal
    const proposal = proposeMutation(score);

    // IBA governance
    const approved = ibaValidate(proposal);

    // Memory event
    const memoryEvent = {
        input,
        output,
        score,
        proposal,
        approved,
        timestamp: new Date().toISOString()
    };

    console.log("Memory Event:", memoryEvent);

    // Render
    document.getElementById("runtimeOutput").innerHTML = `
        <p><strong>Input:</strong> ${input}</p>
        <p><strong>Output:</strong> ${output}</p>
        <p><strong>Score:</strong> ${score}</p>
        <p><strong>Mutation:</strong> ${proposal.action}</p>
        <p><strong>Strategy:</strong> ${proposal.strategy}</p>
        <p><strong>IBA:</strong> ${
            approved ? "approved" : "blocked"
        }</p>
    `;
}
