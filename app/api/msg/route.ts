async function handler() {
  return Response.json(
    {
      msg: [],
      deprecated: true,
    },
    { status: 202 }
  );
}

export { handler as GET, handler as POST };
