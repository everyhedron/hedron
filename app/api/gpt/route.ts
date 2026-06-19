const deprecatedMessage = "This interactive AI response is currently unavailable.";

async function handler() {
  return Response.json(
    {
      msg: deprecatedMessage,
      tid: "ai-deprecated",
      deprecated: true,
    },
    { status: 202 }
  );
}

export { handler as GET, handler as POST };
