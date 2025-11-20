
export function ShortTeamInfo({ name }) {

  const result = name.slice(0, n);
  return (
    <div className="short-team-info-div">
      <p>{"Team " + name}</p>
    </div>
  );
}
